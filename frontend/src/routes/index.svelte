<script>
	import { Link } from '@sveltejs/kit';
</script>

<main>
	<h1>Welcome to the Home Page!</h1>
	<p>
		Go to <Link to="/login">Login Page</Link>
	</p>
</main>

<style>
	main {
		text-align: center;
	}

	a {
		text-decoration: none;
		color: blue;
		font-weight: bold;
	}
</style>
