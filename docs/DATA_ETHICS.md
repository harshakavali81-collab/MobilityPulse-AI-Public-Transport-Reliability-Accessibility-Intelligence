# Data provenance, safety and accessibility

**This is a portfolio application, not a public transit service.**

- Default route names and stop coordinates represent fictional Sample City; do not navigate with them.
- All default stop events are generated deterministically from seed 42. The demo metrics measure those generated events only.
- Real GTFS Schedule ZIPs contain planned timetables and geographic descriptions. They do not inherently provide actual arrivals.
- A separate historical observation file can contain actual arrivals, but this code cannot verify whether externally supplied claims are genuine. Source provenance and permissions must be checked manually.
- In GTFS, `wheelchair_boarding=0` is unknown, `1` is publisher-reported availability, `2` is publisher-reported absence. These codes alone do not guarantee accessibility.
- The optional GTFS-RT parser is a local diagnostic. Without an agency-authorized real-time feed, the UI explicitly indicates no live tracking.
- Offline RandomForest metrics from synthetic samples must never be presented as real-world predictive accuracy or used for travel safety.
- No passenger identifiers, personal locations, or surveillance data should be ingested without appropriate legal basis and privacy review.
- Verify GTFS license, feed freshness, agency terms, security and appropriate data retention before deploying for public use.
