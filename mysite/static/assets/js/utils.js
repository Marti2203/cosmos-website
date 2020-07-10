function getParameterByName(name, url = window.location.href) {
    let name_replaced = name.replace(/[\[\]]/g, "\\$&");
    let regex = new RegExp(`[?&]${name_replaced}(=([^&#]*)|&|#|$)`),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}