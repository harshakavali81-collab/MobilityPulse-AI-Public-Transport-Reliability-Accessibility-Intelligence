from mobilitypulse.analytics.on_time_performance import summary

def by_route(rows,routes):
    result=[]
    for r in routes:
        metrics=summary([x for x in rows if x["route_id"]==r["route_id"]])
        result.append({"route_id":r["route_id"],"route_short_name":r["route_short_name"],
            "route_long_name":r["route_long_name"],"route_color":r.get("route_color","#64748b"),**metrics})
    return result
