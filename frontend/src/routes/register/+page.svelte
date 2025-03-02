<script>
	import { onMount } from 'svelte';

	let username = '';
	let email = '';
	let password1 = '';
	let password2 = '';
	let errorMessage = '';
	let successMessage = '';

	// Function to handle form submission
	const handleSubmit = async () => {
		// Reset messages
		errorMessage = '';
		successMessage = '';

		// Check if passwords match
		if (password1 !== password2) {
			errorMessage = 'Passwords do not match!';
			return;
		}

		// Data to be sent to the backend
		const registrationData = {
			username,
			email,
			password1,
			password2
		};

		try {
			// Make POST request to the backend registration endpoint
			const response = await fetch('/api/auth/registration/', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify(registrationData)
			});

			if (!response.ok) {
				// If the server responds with an error
				const errorData = await response.json();
				errorMessage = errorData.message || 'Registration failed. Please try again.';
				alert(errorMessage);
			} else {
				// If registration is successful
				const data = await response.json();
				successMessage = data.message || 'Registration successful! Please log in.';
				alert(successMessage);
			}
		} catch (error) {
			// Handle any network errors
			errorMessage = 'Network error. Please try again later.';
		}
	};
</script>

<div class="side-container">
	<div class="side-content">
		<!-- Registration Form -->
		<div class="registration-form">
			<h1>Register</h1>

			<form on:submit|preventDefault={handleSubmit}>
				<input type="username" placeholder="Username" bind:value={username} required />
				<input type="email" placeholder="Email" bind:value={email} required />
				<input type="password" placeholder="Password" bind:value={password1} required />
				<input type="password" placeholder="Confirm Password" bind:value={password2} required />
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
	@import '$assets/styles/registration.css';
</style>
