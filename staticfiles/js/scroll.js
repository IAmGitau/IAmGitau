document.addEventListener('DOMContentLoaded', () => {
    window.onscroll = () => {
        ScrollFunction();
    };

    let header = document.getElementById("Dheader");

    function ScrollFunction() {
        let height = 15;
        if (document.body.scrollTop >= height || document.documentElement.scrollTop >= height) {
            header.style.boxShadow = "0.5rem .24rem .25rem 0 rgba(100, 110, 140, .2)";
        } else {
            header.style.boxShadow = "none";
        }
    }
});
