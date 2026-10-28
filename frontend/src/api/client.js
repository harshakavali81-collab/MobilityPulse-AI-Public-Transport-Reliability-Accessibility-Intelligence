/** API client. In GitHub Pages, use the built-in frozen synthetic snapshot. */
const base=(import.meta.env.VITE_API_URL||'').replace(/\/$/,'');
const staticMode=import.meta.env.VITE_STATIC_DEMO==='true';
export async function api(path){
  const endpoint=staticMode
    ? import.meta.env.BASE_URL+'sample-api'+path+'.json'
    : base+'/api'+path;
  const response=await fetch(endpoint,{headers:{Accept:'application/json'}});
  if(!response.ok)throw new Error('API '+response.status+': '+path);
  return response.json();
}
export const getOverview=()=>api('/overview');
export const getRoutes=()=>api('/routes');
export const getStops=()=>api('/stops');
export const getReliability=()=>api('/analytics/reliability');
export const getTrends=()=>api('/analytics/trends');
export const getHeadways=()=>api('/analytics/headways');
export const getAccessibility=()=>api('/accessibility');
export const getFeed=()=>api('/feed/status');
