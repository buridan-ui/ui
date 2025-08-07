import reflex as rx


def download_site_source():
    return rx.el.div(
        rx.el.label(
            "Download Repo",
            color=rx.color("slate", 12),
            class_name="text-sm font-regular",
        ),
        rx.box(
            rx.el.label(
                "",
                id="countdown-text",
                class_name="text-xs p-0 m-0",
                title="Download cooldown",
            ),
            rx.el.button(
                rx.icon(
                    tag="download",
                    size=11,
                    color=rx.color("slate", 11),
                    id="download-icon",
                ),
                id="download-button",
                on_click=rx.call_script(
                    """
                    const button = document.getElementById('download-button');
                    const iconElement = document.getElementById('download-icon');
                    const countdownElement = document.getElementById('countdown-text');
                    const repoUrl = 'https://github.com/buridan-ui/ui/archive/refs/heads/main.zip'; 

                    // Set cooldown duration in seconds
                    const cooldownDuration = 60;

                    // Store the end time in localStorage
                    const endTime = Date.now() + (cooldownDuration * 1000);
                    localStorage.setItem('downloadCooldownEnd', endTime.toString());

                    // Disable the button
                    button.disabled = true;

                    // Open the ZIP file in a new tab
                    window.open(repoUrl, '_blank');

                    // Hide the icon and start countdown
                    iconElement.style.display = 'none';
                    updateCountdown();

                    function updateCountdown() {
                        const now = Date.now();
                        const storedEndTime = parseInt(localStorage.getItem('downloadCooldownEnd') || '0');

                        if (storedEndTime > now) {
                            // Countdown still active
                            const secondsLeft = Math.ceil((storedEndTime - now) / 1000);
                            countdownElement.textContent = secondsLeft.toString();
                            button.disabled = true;

                            // Check again in 1 second
                            setTimeout(updateCountdown, 1000);
                        } else {
                            // Countdown complete
                            button.disabled = false;
                            iconElement.style.display = '';
                            countdownElement.textContent = '';
                            localStorage.removeItem('downloadCooldownEnd');
                        }
                    }
                    """
                ),
                on_mount=rx.call_script(
                    """
                    // Check for existing cooldown on page load
                    const button = document.getElementById('download-button');
                    const iconElement = document.getElementById('download-icon');
                    const countdownElement = document.getElementById('countdown-text');

                    function checkExistingCooldown() {
                        const now = Date.now();
                        const storedEndTime = parseInt(localStorage.getItem('downloadCooldownEnd') || '0');

                        if (storedEndTime > now) {
                            // Countdown still active
                            const secondsLeft = Math.ceil((storedEndTime - now) / 1000);
                            countdownElement.textContent = secondsLeft.toString();
                            button.disabled = true;
                            iconElement.style.display = 'none';

                            // Start the update function
                            updateCountdown();
                        }
                    }

                    function updateCountdown() {
                        const now = Date.now();
                        const storedEndTime = parseInt(localStorage.getItem('downloadCooldownEnd') || '0');

                        if (storedEndTime > now) {
                            // Countdown still active
                            const secondsLeft = Math.ceil((storedEndTime - now) / 1000);
                            countdownElement.textContent = secondsLeft.toString();
                            button.disabled = true;

                            // Check again in 1 second
                            setTimeout(updateCountdown, 1000);
                        } else {
                            // Countdown complete
                            button.disabled = false;
                            iconElement.style.display = '';
                            countdownElement.textContent = '';
                            localStorage.removeItem('downloadCooldownEnd');
                        }
                    }

                    // Run on page load
                    checkExistingCooldown();
                    """
                ),
            ),
            _hover={"background": rx.color("gray", 3)},
            border=f"0.81px solid {rx.color('gray', 5)}",
            class_name="flex flex-row cursor-pointer rounded-md flex items-center justify-center align-center p-1",
        ),
        class_name="w-full flex flex-row justify-between align-center items-center",
    )
