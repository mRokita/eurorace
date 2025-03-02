<script>
	let email = '';
	let password = '';
	let confirmPassword = '';
	let errorMessage = '';

	// Function to handle form submission
	const handleSubmit = () => {
		// Handle the registration logic here
		if (password !== confirmPassword) {
			errorMessage = 'Passwords do not match!';
			return;
		}

		console.log('Registration details:', { email, password });
	};
</script>

<div class="side-container">
	<div class="side-content">
		<!-- Registration Form -->
		<div class="registration-form">
			<h1>Register</h1>

			<form on:submit|preventDefault={handleSubmit}>
				<input type="username" placeholder="Username" required />
				<input type="email" placeholder="Email" bind:value={email} required />
				<input type="password" placeholder="Password" bind:value={password} required />
				<input
					type="password"
					placeholder="Confirm Password"
					bind:value={confirmPassword}
					required
				/>
				<input type="submit" value="Register" />
			</form>

			<!-- Error message -->
			{#if errorMessage}
				<p class="error-message">{errorMessage}</p>
			{/if}

			<!-- Redirect to login -->
			<p>Already have an account? <a href="/login">Login here</a></p>
		</div>
	</div>

	<div class="side-content">
		<!-- You can add an image or background here -->
	</div>
</div>

<!-- Import the registration CSS -->
<style>
	@import '../../assets/styles/registration.css';
</style>
