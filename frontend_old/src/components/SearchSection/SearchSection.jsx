import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { setFiltered, clearFiltered } from '../../slices/cardsSlice/cardsSlice';

import { cardsArray } from '../../utils/cardsArray';

// import cn from 'classnames';

import styles from './SearchSection.module.scss';
import Button from '../../assets/ui-kit/Button/Button';
import SearchResult from '../SearchResult/SearchResult';

function SearchSection() {
	const dispatch = useDispatch();
	const navigate = useNavigate();

	const [inputValue, setInputVlaue] = useState('');
	const [placeholder, setPlaceholder] = useState('Название кофеӣни / адрес');
	const [isQuery, setIsQuery] = useState(false);
	const [isSearchSuccess, setIsSearchSuccess] = useState(false);

	// функция фильтрации карточек
	const onFilter = (inputValue, cardsArray) => {
		localStorage.setItem('inputValue', JSON.stringify(inputValue));
		localStorage.setItem('cards', JSON.stringify(cardsArray));

		// переменная для сохрарения результата поиска
		let searchResult = [];
		if (inputValue) {
			searchResult = cardsArray.filter(item => {
				const searchText =
					item.name.toLowerCase().includes(inputValue.toLowerCase()) ||
					item.address.toLowerCase().includes(inputValue.toLowerCase());
				return searchText;
			});
		}

		searchResult.length > 0 ? setIsSearchSuccess(true) : setIsSearchSuccess(false);
		return searchResult;
	};

	const handleChange = e => {
		!e.target.value ? setIsQuery(false) : setIsQuery(true);
		setInputVlaue(e.target.value);

		// сбрасываем стейт перед новой фильтрацией
		dispatch(clearFiltered());
		const result = onFilter(e.target.value, cardsArray);

		// передаем отфильтрованные карточки в стейт
		dispatch(setFiltered(result));
	};

	const handleSubmit = e => {
		e.preventDefault();
		if (!isQuery) {
			setPlaceholder('Нужно ввести ключевое слово');
		} else {
			const result = onFilter(inputValue, cardsArray);

			dispatch(clearFiltered());
			dispatch(setFiltered(result));
			setIsSearchSuccess(false);
			navigate('/');
		}
	};

	return (
		<section className={styles.container}>
			<div className={styles.input_container}>
				<input
					className={styles.input}
					placeholder={placeholder}
					value={inputValue}
					onChange={handleChange}
				/>
				<SearchResult isVisible={isSearchSuccess} />
			</div>
			<Button onClick={handleSubmit} text="найти" size="small" />
		</section>
	);
}

export default SearchSection;
