import io,zipfile
import pandas as pd
import pytest
from mobilitypulse.processing.validate_gtfs import validate
from mobilitypulse.ingestion.gtfs_static_loader import load_gtfs_zip,to_catalog
def make_zip(path,broken=False):
    files={
      "agency.txt":"agency_name,agency_url,agency_timezone\nTest,http://example.org,UTC\n",
      "routes.txt":"route_id,route_type,route_short_name\nR1,3,Blue\n",
      "stops.txt":"stop_id,stop_name,stop_lat,stop_lon,wheelchair_boarding\nS1,Central,17.5,78.5,0\n",
      "trips.txt":"route_id,service_id,trip_id\nR1,WKD,T1\n",
      "stop_times.txt":"trip_id,arrival_time,departure_time,stop_id,stop_sequence\nT1,09:00:00,09:00:00,S2,1\n" if broken else "trip_id,arrival_time,departure_time,stop_id,stop_sequence\nT1,09:00:00,09:00:00,S1,1\n"}
    with zipfile.ZipFile(path,"w") as z:
      for name,value in files.items():z.writestr(name,value)
def test_load_valid_gtfs(tmp_path):
    p=tmp_path/"feed.zip";make_zip(p)
    data=to_catalog(load_gtfs_zip(p))
    assert len(data["routes"])==1
    assert data["metadata"]["data_mode"]=="schedule_only"
    assert data["observations"]==[]
def test_dangling_stop_rejected(tmp_path):
    p=tmp_path/"feed.zip";make_zip(p,broken=True)
    with pytest.raises(ValueError,match="dangling"):load_gtfs_zip(p)
def test_missing_required_file():
    errors=validate({"routes.txt":pd.DataFrame({"route_id":["R1"]})})
    assert any("missing" in e for e in errors)
def test_invalid_latitude():
    frames={}
    for k,cols in __import__("mobilitypulse.processing.validate_gtfs",fromlist=["REQUIRED"]).REQUIRED.items():
      frames[k]=pd.DataFrame([{c:"x" for c in cols}])
    for k in ["route_id","trip_id","stop_id"]:
      for table in frames:
        if k in frames[table].columns:frames[table][k]="A"
    frames["stops.txt"]["stop_lat"]="900"
    frames["stops.txt"]["stop_lon"]="78.5"
    assert any("invalid stop_lat" in e for e in validate(frames))
