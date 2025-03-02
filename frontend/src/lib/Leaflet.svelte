<script lang="ts">

  import L from 'leaflet';
	import 'leaflet/dist/leaflet.css';
  import { onDestroy, onMount, setContext } from 'svelte';

	let map: L.Map | undefined;
	let mapElement: HTMLDivElement;
  export let bounds: L.LatLngBoundsExpression | undefined = undefined;
  export let view: L.LatLngExpression | undefined = undefined;
  export let zoom: number | undefined = undefined;
  onMount(() => {
    map = L.map(mapElement).setView([52.25, 20.9], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(map);
  });

  onDestroy(() => {
    map?.remove();
    map = undefined;
  });

  setContext('map', {
    getMap: () => map
  });

  $: if (map) {
    if (bounds) {
      map.fitBounds(bounds);
    } else if (view && zoom) {
      map.setView(view, zoom);
    }
  }

</script>

<div class="w-full h-full" bind:this={mapElement}>
  <slot />
</div>