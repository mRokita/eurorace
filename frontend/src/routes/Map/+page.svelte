<script lang="ts">
	import '../../app.css';
	import type { LatLngExpression } from 'leaflet';
	import Leaflet from '$lib/Leaflet.svelte'; // Ensure this path is correct
	import Marker from '$lib/Marker.svelte'; // Ensure this path is correct

	const initialView: LatLngExpression = [52.25, 20.9];
	const markerLocations: Array<LatLngExpression> = [
		[52.25, 20.9],
	];
</script>

<div class="w-full h-screen">
	<Leaflet view={initialView} zoom ={13}>
		{#each markerLocations as latLng}
			<Marker {latLng} width={40} height={40}/>
		{/each}
	</Leaflet>
</div>