import axios from "axios";

const domain = "http://127.0.0.1:5000";

export const HTTP_METHODS = {
	POST: 'POST',
	GET: 'GET',
};

export const HttpRequest = async (url, method = 'GET', data = null) => {
	try {
		if (method === 'POST' && (data === null || data === undefined)) {
			throw new Error(`Body is mandatory for POST Call`);
		}
		const config = {
			method: method,
			url: domain + url,
			headers: {
				'Content-Type': 'application/json'
			}
		};
		const token = localStorage.getItem("token");
		if(token) {
			config.headers['Authorization'] = 'Bearer ' + token
		}
		if (method === 'POST') {
			config.data = data;
		}
		const response = await axios(config);
		return response.data;

	} catch (error) {
		if (error.response) {
			console.log(error.response.data);
			return error.response.data;
		} else if (error.request) {
			console.log('No response received:', error.request);
			return error.request;
		} else {
			console.log('Error:', error.message);
		}
	}
};