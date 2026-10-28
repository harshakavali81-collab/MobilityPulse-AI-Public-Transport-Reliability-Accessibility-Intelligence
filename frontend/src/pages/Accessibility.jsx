import React,{useState} from 'react';
export default function AccessibilityPage({data}){
 const [filter,setFilter]=useState('all');
 const counts={accessible:0,inaccessible:0,unknown:0};
 for(const x of data.accessibility){const k=+x.wheelchair_boarding===1?'accessible':+x.wheelchair_boarding===2?'inaccessible':'unknown';counts[k]++}
 const filtered=data.accessibility.filter(s=>filter==='all'||(+s.wheelchair_boarding===1?'accessible':+s.wheelchair_boarding===2?'inaccessible':'unknown')===filter);
 return <section><div className="eyebrow">ACCESSIBILITY INTELLIGENCE</div><div className="page-title"><div><h1>Access matters<span className="accent">.</span></h1><p>Publisher-reported wheelchair boarding metadata with unknowns preserved.</p></div></div>
 <div className="notice">GTFS wheelchair_boarding=0 means unknown — not accessible. Conditions must be verified with the transit operator.</div>
 <div className="stats three">{Object.entries(counts).map(([k,v])=><button key={k} className={'stat filter-card '+(filter===k?'selected':'')} onClick={()=>setFilter(filter===k?'all':k)}><div>{k.toUpperCase()}</div><strong>{v}</strong><small>Sample stops</small></button>)}</div>
 <article className="panel"><div className="panel-title"><h2>Stop accessibility register</h2><span className="tag">SOURCE ATTRIBUTION</span></div><div className="table-scroll"><table><thead><tr><th>Stop name</th><th>Stop ID</th><th>Reported status</th></tr></thead><tbody>{filtered.map(s=><tr key={s.stop_id}><td>{s.stop_name}</td><td>{s.stop_id}</td><td><span className={'status '+(+s.wheelchair_boarding===1?'good':+s.wheelchair_boarding===2?'bad':'unknown')}>{s.wheelchair_status.replaceAll('_',' ')}</span></td></tr>)}</tbody></table></div></article></section>
}
