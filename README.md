# myflight
Microservice-based application to monitor the status of your flight in *almost* real time

# Goals
- [x] Add flights to the database
- [x] Fetch flight data
- [ ] Display approximate arrival time
- [ ] Display route on the map
- [ ] Notify when airplane lands or is delayed

# Stack
- Python 3
- Flask
- SQLAlchemy
- Airlabs API
- PostGIS

# Disclaimer
This project is for *home use only*. To use Flight Radar API commercially, you need to subscribe to Business plan.

# Notes
In order to use this project, you need to sign up for a free acount on [airlabs.co](https://airlabs.co) and create a file `.airlabs` with
the following content:
```
AIRLABS_API_KEY=<you key>
```