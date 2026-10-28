const base=(import.meta.env.VITE_API_URL||'').replace(/\/$/,'');
export async function api(path){
  const response=await fetch(base+'/api'+path);
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
