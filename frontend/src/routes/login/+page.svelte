<script>
	let email = '';
	let password = '';

	// Function to handle form submission
	const handleSubmit = () => {
		// Handle the login logic here
		console.log('Login details:', { email, password });
	};
</script>

<div class="side-container">
	<div class="side-content">
		<!-- Login Form -->
		<div class="login-form">
			<h1>Login</h1>

			<form on:submit|preventDefault={handleSubmit}>
				<input type="email" placeholder="Email" bind:value={email} required />
				<input type="password" placeholder="Password" bind:value={password} required />
				<input type="submit" value="Login" />
			</form>

			<!-- Forgot password link -->
			<a href="#" class="forgot-password">Forgot Password?</a>
		</div>
	</div>
	<div class="side-content">
		<!-- You can add an image or background here -->
	</div>
</div>

<!-- Import the login CSS -->
<style>
	@import '../../assets/styles/login.css';
</style>
