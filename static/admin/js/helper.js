// Helper function to get cookie value
export function getCookie(name) {
    const cookieName = encodeURIComponent(name) + '=';
    const cookieArray = document.cookie.split(';');
    for (let i = 0; i < cookieArray.length; i++) {
        let cookie = cookieArray[i];
        while (cookie.charAt(0) === ' ') {
            cookie = cookie.substring(1);
        }
        if (cookie.indexOf(cookieName) === 0) {
            return decodeURIComponent(cookie.substring(cookieName.length));
        }
    }
    return '';
}

// Helper function to set cookie value
export function setCookie(name, value, days = 365) {
    const expires = new Date();
    expires.setTime(expires.getTime() + (days * 24 * 60 * 60 * 1000));
    document.cookie = encodeURIComponent(name) + '=' + encodeURIComponent(value) + ';expires=' + expires.toUTCString() + ';path=/';
}

