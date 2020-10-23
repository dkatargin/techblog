export default function Fetcher(uri, request_method, callback) {
    if(!uri){
        console.error('URI is null');
        return
    }

    const full_uri = `http://exobook:8000${uri}`

    const req_params = {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
    };

    fetch(full_uri, req_params)
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
