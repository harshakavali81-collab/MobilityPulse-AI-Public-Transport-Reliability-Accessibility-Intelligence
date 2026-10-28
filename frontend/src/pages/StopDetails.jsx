import React,{useState} from 'react';
export default function StopDetails({data,selectedStop,setSelectedStop}){
 const [query,setQuery]=useState('');
 const stops=data.stops.filter(s=>s.stop_name.toLowerCase().includes(query.toLowerCase()));
 const s=selectedStop||stops[0];
 const lines=s?data.routes.filter(r=>r.stop_ids.includes(s.stop_id)):[];
 const status=Number(s?.wheelchair_boarding)===1?'Publisher reports accessible':Number(s?.wheelchair_boarding)===2?'Publisher reports inaccessible':'Accessibility unknown';
 return <section><div className="eyebrow">STOP INFORMATION</div><div className="page-title"><div><h1>Stop directory<span className="accent">.</span></h1><p>Location metadata and route connectivity, with clear accessibility caveats.</p></div></div>
 <div className="layout-two stops-layout"><article className="panel"><div className="panel-title"><h2>Search stops</h2><span className="tag">{stops.length} FOUND</span></div><input className="search-input" placeholder="Search stops by name…" value={query} onChange={e=>setQuery(e.target.value)}/><div className="scroll-list">{stops.map(x=><button className={s?.stop_id===x.stop_id?'selected':''} onClick={()=>setSelectedStop(x)} key={x.stop_id}>{x.stop_name}<span>{x.stop_id}</span></button>)}</div></article>
 <article className="panel">{s?<><div className="panel-title"><h2>{s.stop_name}</h2><span className="tag">{s.stop_id}</span></div><div className="detail-grid"><div><small>Latitude</small><strong>{s.stop_lat}</strong></div><div><small>Longitude</small><strong>{s.stop_lon}</strong></div><div><small>Accessibility</small><strong>{status}</strong></div><div><small>Routes serving stop</small><strong>{lines.length}</strong></div></div><h3>Connected routes</h3>{lines.map(r=><div key={r.route_id} className="item-line"><span className="route-square" style={{background:r.route_color}}>{r.route_short_name}</span>{r.route_long_name}</div>)}<div className="help-note">These stops and coordinates are fictional. Never use for travel.</div></>:<p>No matching stops.</p>}</article></div></section>
}
