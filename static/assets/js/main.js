/*
	Solid State by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

(function($) {



	



	var	$window = $(window),
		$body = $('body'),
		$header = $('#header'),
		$banner = $('#banner');

	// Breakpoints.
		breakpoints({
			xlarge:	'(max-width: 1680px)',
			large:	'(max-width: 1280px)',
			medium:	'(max-width: 980px)',
			small:	'(max-width: 736px)',
			xsmall:	'(max-width: 480px)'
		});

	// Play initial animations on page load.
		$window.on('load', function() {
			window.setTimeout(function() {
				$body.removeClass('is-preload');
			}, 100);
		});

	// Header.
		if ($banner.length > 0
		&&	$header.hasClass('alt')) {

			$window.on('resize', function() { $window.trigger('scroll'); });

			$banner.scrollex({
				bottom:		$header.outerHeight(),
				terminate:	function() { $header.removeClass('alt'); },
				enter:		function() { $header.addClass('alt'); },
				leave:		function() { $header.removeClass('alt'); }
			});

		}

	// Menu.
		var $menu = $('#menu');

		$menu._locked = false;

		$menu._lock = function() {

			if ($menu._locked)
				return false;

			$menu._locked = true;

			window.setTimeout(function() {
				$menu._locked = false;
			}, 350);

			return true;

		};

		$menu._show = function() {

			if ($menu._lock())
				$body.addClass('is-menu-visible');

		};

		$menu._hide = function() {

			if ($menu._lock())
				$body.removeClass('is-menu-visible');

		};

		$menu._toggle = function() {

			if ($menu._lock())
				$body.toggleClass('is-menu-visible');

		};

		$menu
			.appendTo($body)
			.on('click', function(event) {

				event.stopPropagation();

				// Hide.
					$menu._hide();

			})
			.find('.inner')
				.on('click', '.close', function(event) {

					event.preventDefault();
					event.stopPropagation();
					event.stopImmediatePropagation();

					// Hide.
						$menu._hide();

				})
				.on('click', function(event) {
					event.stopPropagation();
				})
				.on('click', 'a', function(event) {

					var href = $(this).attr('href');

					event.preventDefault();
					event.stopPropagation();

					// Hide.
						$menu._hide();

					// Redirect.
						window.setTimeout(function() {
							window.location.href = href;
						}, 350);

				});

		$body
			.on('click', 'a[href="#menu"]', function(event) {

				event.stopPropagation();
				event.preventDefault();

				// Toggle.
					$menu._toggle();

			})
			.on('keydown', function(event) {

				// Hide on escape.
					if (event.keyCode == 27)
						$menu._hide();

			});

			//Code for containers and image slider:
	// Get the carousel element
	let carousel = document.querySelector('.carousel')
	// Get the buttons
	let prev = carousel.querySelector('button.prev')
	let next = carousel.querySelector('button.next')
	// Get all images
	let images = carousel.querySelectorAll('.images img')
	// Starting index of the carousel
	let index = 0

	// Function to update the carousel when clicking a button
	function updateImage(direction) {
	// Different handling based on if you clicked previous or next
	if (direction === 'prev') {
		// When clicking previous: Decrease index when its higher than 0
		index = index > 0 ? index - 1 : index
		// Disable button if index is 0
		prev.disabled = index === 0
		// Enable next
		next.disabled = false
	} else {
		// When clicking next: Increase when lower than img amount
		index = index < images.length - 1 ? index + 1 : index
		// Increase when lower than img amount
		next.disabled = index === images.length - 1
		// Enable previous
		prev.disabled = false
	}
	// Get the previous image
	let current = carousel.querySelector('.images img.current')
	// Hide the previous image
	if(current) current.classList.remove('current')
	// Show current image
	images[index].classList.add('current')
	}
	// Event listeners for previous
	prev.addEventListener('click', () => updateImage('prev'))
	// Event listeners for next
	next.addEventListener('click', updateImage)





})(jQuery);