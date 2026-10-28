import React from 'react';
import {ArrowUpRight,Activity,Clock3,MapPinned,BusFront,AlertTriangle,ShieldCheck} from 'lucide-react';
import {DailyChart,RouteBars} from '../components/Charts.jsx';
import RouteMap from '../components/RouteMap.jsx';
const value=(v,s='')=>v===null||v===undefined?'N/A':v+s;
export default function Dashboard({data,onOpenRoute}){
 const o=data.overview;return <section>
 <div className="eyebrow">SYNTHETIC SAMPLE CITY / OPERATIONS OVERVIEW</div>
 <div className="page-title"><div><h1>Transit network overview<span className="accent">.</span></h1><p>Routes, on-time performance and service patterns in one intelligent workspace.</p></div><button className="primary" onClick={onOpenRoute}>Explore routes <ArrowUpRight size={16}/></button></div>
 <div className="notice"><ShieldCheck size={18}/><div><b>Transparent data provenance</b><span>All default events and map locations are synthetic. No live arrival, cancellation or accessibility certification is provided.</span></div></div>
 <div className="stats">
 <div className="stat"><div><BusFront size={20}/> Active demo routes</div><strong>{o.routes}</strong><small>Fictional service network</small></div>
 <div className="stat"><div><MapPinned size={20}/> Mapped stops</div><strong>{o.stops}</strong><small>Sample City coordinates</small></div>
 <div className="stat"><div><Activity size={20}/> Observed on time</div><strong>{value(o.reliability.on_time_pct,'%')}</strong><small>Demo stop-level observations</small></div>
 <div className="stat"><div><Clock3 size={20}/> Mean delay</div><strong>{value(o.reliability.mean_delay_minutes,' min')}</strong><small>Observed demo events only</small></div>
 </div>
 <div className="layout-two"><article className="panel map-card"><div className="panel-title"><div><h2>Network route explorer</h2><p>Geographic schematic · fictional Sample City</p></div><span className="tag">MAP VIEW</span></div><RouteMap routes={data.routes} stops={data.stops}/></article>
 <article className="panel"><div className="panel-title"><div><h2>Route reliability</h2><p>On-time percentage by route</p></div><span className="tag">SYNTHETIC</span></div><RouteBars data={data.reliability}/></article></div>
 <div className="layout-two"><article className="panel"><div className="panel-title"><div><h2>Daily performance trend</h2><p>Historical synthetic stop observations</p></div><span className="tag">21 DAYS</span></div><DailyChart data={data.trends}/></article>
 <article className="panel"><div className="panel-title"><div><h2>Service health</h2><p>Always distinguish scheduled from live events</p></div><span className="tag warn">OFFLINE</span></div><div className="health-cells">
 <div><span>Feed mode</span><strong>{data.feed.mode.replaceAll('_',' ')}</strong></div><div><span>Realtime availability</span><strong>No connected feed</strong></div><div><span>Stop-event cancellations</span><strong>{o.reliability.cancelled_stop_events}</strong></div><div><span>Metadata coverage</span><strong>{data.accessibility.length} stops</strong></div></div><div className="help-note"><AlertTriangle size={17}/>Cancellation counts are stop events, not unique cancelled trips.</div></article></div>
 </section>
}
