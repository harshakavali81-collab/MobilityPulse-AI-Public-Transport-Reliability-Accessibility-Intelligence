import React,{useState} from 'react';
import RouteMap from '../components/RouteMap.jsx';
export default function RouteExplorer({data,selectStop}){
 const [selected,setSelected]=useState(null);
 return <section><div className="eyebrow">DISCOVER NETWORK</div><div className="page-title"><div><h1>Route explorer<span className="accent">.</span></h1><p>Compare fictional routes and navigate their stop patterns.</p></div></div>
 <div className="notice">Route lines are illustrative and do not represent navigable live services.</div>
 <div className="layout-two route-layout"><article className="panel"><div className="panel-title"><h2>Sample network</h2><span className="tag">4 ROUTES</span></div><RouteMap routes={data.routes} stops={data.stops} selected={selected} onSelect={selectStop}/></article>
 <article className="panel"><div className="panel-title"><h2>Routes</h2><span className="tag">SELECT ONE</span></div><div className="routes-list">{data.routes.map(r=><button className={'route-list-item '+(selected===r.route_id?'selected':'')} key={r.route_id} onClick={()=>setSelected(selected===r.route_id?null:r.route_id)}><span className="route-square" style={{background:r.route_color}}>{r.route_short_name}</span><span><strong>{r.route_long_name}</strong><small>{(r.stop_ids||[]).length} stops · Synthetic sample</small></span><span>→</span></button>)}</div>
 {selected&&<div className="selected-list"><h3>Stops on {selected}</h3>{data.routes.find(r=>r.route_id===selected)?.stop_ids.map((id,i)=>{const s=data.stops.find(x=>x.stop_id===id);return s&&<button key={id} onClick={()=>selectStop(s)}>{String(i+1).padStart(2,'0')} · {s.stop_name} <span>View ›</span></button>})}</div>}</article></div></section>
}
