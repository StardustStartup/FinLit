<template>
  <div class="App"/>
</template>

<script>
import MarkerClusterer from '@google/markerclusterer';

import gmapsInit from './utils/gmaps';

const locations = [
  {
    position: {
      lat: 42.3497,
      lng: -71.1068,
    },
  },
  {
    position: {
      lat: 42.3499,
      lng: -71.1080,
    },
  },
  {
    position: {
      lat: 42.3480,
      lng: -71.1100,
    },
  },
  {
    position: {
      lat: 42.3460,
      lng: -71.1060,
    },
  },
  {
    position: {
      lat: 42.3490,
      lng: -71.1068,
    },
  },
  {
    position: {
      lat: 42.3460,
      lng: -71.1050,
    },
  },
];

export default {
  name: `App`,
  async mounted() {
    try {
      const google = await gmapsInit();
      const geocoder = new google.maps.Geocoder();
      const map = new google.maps.Map(this.$el);

      geocoder.geocode({ address: `Boston` }, (results, status) => {
        if (status !== `OK` || !results[0]) {
          throw new Error(status);
        }

        map.setCenter(results[0].geometry.location);
        map.fitBounds(results[0].geometry.viewport);
      });

      const markerClickHandler = (marker) => {
        map.setZoom(13);
        map.setCenter(marker.getPosition());
      };

      const markers = locations
        .map((location) => {
          const marker = new google.maps.Marker({ ...location, map });
          marker.addListener(`click`, () => markerClickHandler(marker));

          return marker;
        });

      // eslint-disable-next-line no-new
      new MarkerClusterer(map, markers, {
        imagePath: `https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m`,
      });
    } catch (error) {
      // eslint-disable-next-line no-console
      console.error(error);
    }
  },
};
</script>

<style>
html,
body {
  margin: 0;
  padding: 0;
}

.App {
  width: 100vw;
  height: 100vh;
}
</style>
