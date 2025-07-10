document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("login-form");
    const errorDisplay = document.getElementById("error");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const username = document.getElementById("username").value.trim();
        const password = document.getElementById("password").value.trim();

        try {
            const response = await fetch("/api/v1/token/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({username, password}),
            });

            const data = await response.json();

            if (response.ok) {
                // Save tokens in localStorage
                localStorage.setItem("access", data.access);
                localStorage.setItem("refresh", data.refresh);
                localStorage.setItem("user", data.user.id)

                // Redirect to dashboard
                window.location.href = "/dashboard/";
            } else {
                // Show error message
                errorDisplay.textContent = data.detail;
            }
        } catch (error) {
            console.error("Login error:", error);
            errorDisplay.textContent = "An unexpected error occurred.";
        }
    });
});
