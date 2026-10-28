import React,{useState,useEffect} from 'react';
import {LayoutDashboard,Route,MapPin,ChartNoAxesCombined,Accessibility,Activity,TrainFront,PanelLeftClose,AlertCircle,ExternalLink} from 'lucide-react';
import Dashboard from './pages/Dashboard.jsx';
import RouteExplorer from './pages/RouteExplorer.jsx';
import StopDetails from './pages/StopDetails.jsx';
import Reliability from './pages/Reliability.jsx';
import AccessPage from './pages/Accessibility.jsx';
import FeedStatus from './pages/FeedStatus.jsx';
import {getOverview,getRoutes,getStops,getReliability,getTrends,getHeadways,getAccessibility,getFeed,getPredictions} from './api/client.js';
const tabs=[['dashboard','Overview',LayoutDashboard],['routes','Route explorer',Route],['stops','Stop details',MapPin],['reliability','Reliability',ChartNoAxesCombined],['accessibility','Accessibility',Accessibility],['feed','Feed health',Activity]];
export default function App(){
 const [tab,setTab]=useState('dashboard'),[data,setData]=useState(null),[error,setError]=useState(''),[loading,setLoading]=useState(true),[selectedStop,setSelectedStop]=useState(null),[collapsed,setCollapsed]=useState(false);
 useEffect(()=>{let active=true;Promise.all([getOverview(),getRoutes(),getStops(),getReliability(),getTrends(),getHeadways(),getAccessibility(),getFeed(),getPredictions()]).then(([overview,routes,stops,reliability,trends,headways,accessibility,feed,predictions])=>{if(active){setData({overview,routes:routes.items,stops:stops.items,reliability:reliability.items,trends:trends.items,headways:headways.items,accessibility:accessibility.items,feed,predictions});setLoading(false)}}).catch(e=>{if(active){setError(e.message);setLoading(false)}});return()=>{active=false}},[]);
 const pages={dashboard:<Dashboard data={data} onOpenRoute={()=>setTab('routes')}/>,
 routes:<RouteExplorer data={data} selectStop={s=>{setSelectedStop(s);setTab('stops')}}/>,
 stops:<StopDetails data={data} selectedStop={selectedStop} setSelectedStop={setSelectedStop}/>,
 reliability:<Reliability data={data}/>,
 accessibility:<AccessPage data={data}/>,
 feed:<FeedStatus data={data}/>};
 return <div className="shell">
  <aside className={'sidebar '+(collapsed?'collapsed':'')}>
   <div className="brand"><div className="brand-mark"><TrainFront size={23}/></div>{!collapsed&&<span>Mobility<span className="accent">Pulse</span><small>AI INTELLIGENCE</small></span>}</div>
   <div className="nav-section"> {!collapsed&&<p>WORKSPACE</p>}{tabs.map(([key,label,Icon])=><button title={label} className={'nav-item '+(tab===key?'active':'')} key={key} onClick={()=>setTab(key)}><Icon size={19}/>{!collapsed&&label}</button>)}</div>
   <div className="sidebar-bottom">{!collapsed&&<div className="source-card"><span className="source-dot"/> SYNTHETIC DATASET<p>Fictional routes for portfolio demonstration</p></div>}<button className="nav-item" onClick={()=>setCollapsed(!collapsed)} title="Toggle sidebar"><PanelLeftClose size={18}/>{!collapsed&&'Collapse sidebar'}</button></div>
  </aside>
  <main className="main"><header className="topbar"><span className="breadcrumb">TRANSIT INTELLIGENCE <b>/</b> {tabs.find(t=>t[0]===tab)?.[1]}</span><span className="top-right"><span className="demo-pill">● DEMO MODE</span><a href="https://gtfs.org" target="_blank" rel="noreferrer">GTFS docs <ExternalLink size={13}/></a></span></header>
   <div className="content">{loading?<div className="state">Loading transit intelligence…</div>:error?<div className="state error"><AlertCircle/> API unavailable: {error}. Start FastAPI on port 8000 and refresh.</div>:pages[tab]}</div>
   <footer>MobilityPulse AI · Demonstration analytics · No live arrival or verified safety information · © 2026</footer>
  </main>
 </div>
}
