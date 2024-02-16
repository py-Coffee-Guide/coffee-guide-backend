import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import { Provider } from 'react-redux';
import { YMaps } from '@pbe/react-yandex-maps';
import './index.scss';

import App from './components/App/App';
import store from './store';

ReactDOM.createRoot(document.getElementById('root')).render(
	<BrowserRouter>
		<Provider store={store}>
			<YMaps query={{ apikey: 'a0303f06-4ef8-4bd2-bef5-7e2e5e6b3ff6', lang: 'ru_RU' }}>
				<App />
			</YMaps>
		</Provider>
	</BrowserRouter>,
);
