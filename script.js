function showhide() {
    // get the clock
    var myClock = document.getElementById('hide');

    // get the current value of the clock's display property
    var displaySetting = myClock.style.display;

    // also get the clock button, so we can change what it says
    var clockButton = document.getElementById('show-hide');

    // now toggle the clock and the button text, depending on current state
    if (displaySetting == 'none') {
      // clock is visible. hide it
      myClock.style.display = 'block';
      // change button text
      clockButton.innerHTML = 'Learn Less';
    }
    else {
      // clock is hidden. show it
      myClock.style.display = 'none';
      // change button text
      clockButton.innerHTML = 'Learn More';
    }
  }
