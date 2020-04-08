let searchBar = document.getElementById('SearchBar');
let searchIcon = document.getElementById('SearchIcon');

searchIcon.addEventListener('click', () => {
    if (searchBar.style.display === 'block') {
        searchBar.style.display = 'none';
        $('#SearchBar').fadeOut(3000);
    } else {
        searchBar.style.display = 'block';
        $('#SearchBar').fadeIn(3000);
    }
});