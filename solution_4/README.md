## conditions

- Small runways allow planes =< 200,000 pounds
- medium runways allow planes =< 500,000 pounds
- large runway allow any planes
- passengers importance > plane size

## goal

- given an airport
- given a set of planes
- combine planes to runways
- so it takes the least amount of total time 

## math stuff

```shell
runway_s = N
runway_m = N
runway_l = N

total_runways = (runway_s) + (runway_m) + (runway_l)
flights_per_epoch = total_runways

total_time = (flights_per_epoch * total_planes) + (penalty per empty runway per epoch) 
```

Go through every combination until gradient descent for minimum total time is reached. 