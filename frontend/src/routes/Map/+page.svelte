<script lang="ts">
	import '../../app.css';
	import type { LatLngExpression } from 'leaflet';
	import Leaflet from '$lib/Leaflet.svelte'; // Ensure this path is correct
	const initialView: LatLngExpression = [52.25, 20.9];
</script>

<div class="w-full h-screen">
	<Leaflet view={initialView} zoom ={13}/>
</div>