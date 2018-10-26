import axios from 'axios';

export default axios.create({
  baseURL: 'http://localhost:5000/',
  "Access-Control-Allow-Origin": "*",
  'X-Requested-With': 'XMLHttpRequest',
  'X-CSRF-TOKEN' : document.cookie.split('csrftoken=')[1]
});
