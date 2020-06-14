## Fitbit API

A node-JS tool would be constructed to bridge the Fitbit application and the creation of csv's for IBM Cloudant.
<br/><br/>
Within the Fitbit application the following functions will be defined, after defining all permissions:<br/>

### Batched readings of heart rate:

```
import { HeartRateSensor } from "heart-rate";

if (HeartRateSensor) {
  // 1 reading per second, 60 readings per batch
  let hrm = new HeartRateSensor({ frequency: 1, batch: 60 });
  hrm.addEventListener("reading", () => {
    for (let index = 0; index < hrm.readings.timestamp.length; index++) {
      console.log(
        `HeartRateSensor Reading: \
          timestamp=${hrm.readings.timestamp[index]}, \
          [${hrm.readings.bpm[index]}]`
      );
    }
  };
  hrm.start();
}
```

### Detecting Off-Wrist:
```
import { BodyPresenceSensor } from "body-presence";

if (BodyPresenceSensor) {
  const body = new BodyPresenceSensor();
  body.addEventListener("reading", () => {
    if (!body.present) {
      hrm.stop();
    } else {
      hrm.start();
    }
  });
  body.start();
}
```

The ability for trainees to view their own heart rates can be decided by the commander from the fitbit API.

## IBM Chatbot (hands free mode)

Possible commands: "Give me status update on Trainee 76."
This would be a future improvement; the first prototype will only have the database storage function. As detailed in the video pitch, this will be envisioned to be one of the future functions. The database can hence be accessed after linking to the devices.
