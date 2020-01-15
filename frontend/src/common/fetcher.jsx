export default function Fetcher(uri, request_method, callback) {
    if(!uri){
        console.error('URI is null');
        return
    }
    let API_DOMAIN = '';
    if(!uri.startsWith('http')){
        API_DOMAIN = 'http://127.0.0.1:8000';
    }

    const req_params = {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
    };

    fetch(API_DOMAIN + uri, req_params)
        .then(response => {
            if (!response.ok) {
                throw response.json()
            }
            if (response.status === 204) {
                return ''
            }
            return response.json()
        })
        .then(data => {
            callback(data);
        })
        .catch((error) => {
            console.log(error)
        })
}
