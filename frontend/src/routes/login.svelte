<script>
	let email = '';
	let password = '';

	const handleSubmit = () => {
		// Handle the login logic here
		console.log('Login details:', { email, password });
	};
</script>

<div class="side-container">
	<div class="side-content">
		<div class="login-form">
			<h1>Login</h1>

			<form on:submit|preventDefault={handleSubmit}>
				<input type="email" placeholder="Email" bind:value={email} required />
				<input type="password" placeholder="Password" bind:value={password} required />
				<input type="submit" value="Login" />
			</form>

			<a href="#" class="forgot-password">Forgot Password?</a>
		</div>
	</div>
	<div class="side-content">
		<!-- Empty side to add background image -->
	</div>
</div>

<style src="./Login.css"></style>
