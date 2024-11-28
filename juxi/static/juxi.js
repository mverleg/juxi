
/* Timezone */
const tz_cookie_str = 'juxi.timezone=' + Intl.DateTimeFormat().resolvedOptions().timeZone;
if (!document.cookie || !document.cookie.includes(tz_cookie_str)) {
    console.log('setting timezone cookie:', tz_cookie_str)
    document.cookie = tz_cookie_str + "; path=/";
}

