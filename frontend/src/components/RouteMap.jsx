import React from 'react';
const colors=['#32e2cb','#749aff','#fbb77a','#c29cff'];
export default function RouteMap({routes=[],stops=[],selected=null,onSelect=()=>{}}){
 const valid=stops.filter(s=>Number.isFinite(+s.stop_lat)&&Number.isFinite(+s.stop_lon));
 if(!valid.length)return <div className="empty">No georeferenced stops in current feed.</div>;
 const lats=valid.map(s=>+s.stop_lat),lons=valid.map(s=>+s.stop_lon);
 const minLat=Math.min(...lats),maxLat=Math.max(...lats),minLon=Math.min(...lons),maxLon=Math.max(...lons);
 const xy=s=>[64+((+s.stop_lon-minLon)/(maxLon-minLon||1))*772,405-((+s.stop_lat-minLat)/(maxLat-minLat||1))*335];
 const lookup=Object.fromEntries(valid.map(s=>[s.stop_id,s]));
 return <div className="map-panel">
   <div className="map-label">ILLUSTRATIVE NETWORK • NOT NAVIGATION</div>
   <svg viewBox="0 0 900 470" role="img" aria-label="Geographic stop schematic of synthetic transit network">
    <defs><pattern id="grid" width="35" height="35" patternUnits="userSpaceOnUse"><path d="M 35 0 L 0 0 0 35" fill="none" stroke="#1d2b43" strokeWidth="1"/></pattern></defs>
    <rect width="900" height="470" fill="#0c1829"/><rect width="900" height="470" fill="url(#grid)"/>
    {routes.map((r,i)=>{const pts=(r.stop_ids||[]).map(k=>lookup[k]).filter(Boolean).map(xy);
      return pts.length>1?<polyline key={r.route_id} points={pts.map(p=>p.join(',')).join(' ')} fill="none" stroke={r.route_color||colors[i%4]} strokeWidth={selected&&r.route_id!==selected?3:6} opacity={selected&&r.route_id!==selected?.2:.9} strokeLinejoin="round" strokeLinecap="round"/>:null})}
    {valid.map((s,i)=>{const [x,y]=xy(s);return <g key={s.stop_id} onClick={()=>onSelect(s)} tabIndex={0} role="button" aria-label={'Select '+s.stop_name} onKeyDown={e=>{if(e.key==='Enter'||e.key===' ')onSelect(s)}} style={{cursor:'pointer'}}><circle cx={x} cy={y} r="10" fill="#111e33" stroke="#d4faff" strokeWidth="2"/><circle cx={x} cy={y} r="4" fill="#d4faff"/><text x={x+12} y={y-12} fill="#d8e8ff" fontSize="13" fontWeight="600">{s.stop_name}</text></g>})}
   </svg>
   <div className="map-legend">{routes.map((r,i)=><span key={r.route_id}><i style={{background:r.route_color||colors[i%4]}}/>{r.route_short_name}</span>)}</div>
 </div>;
}
