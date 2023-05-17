document.getElementById('aumentar').addEventListener('click', function() {
    let previousClass = classIndex;
    classIndex++;
    classIndex = (classIndex == classes.length) ? classes.length - 1 : classIndex;
    changeClass(previousClass, classIndex);
  });