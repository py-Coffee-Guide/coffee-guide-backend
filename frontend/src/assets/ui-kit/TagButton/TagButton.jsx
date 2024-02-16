import { useState } from 'react';

import cn from 'classnames';
import PropTypes from 'prop-types';
import styles from './TagButton.module.scss';

import { TAG_ICONS } from './TagIcons';

function TagButton({ text, type, tag, theme, active }) {
	const [isActive, setIsActive] = useState(active);
	const { light, dark } = TAG_ICONS[tag];

	const btnClassName = cn(styles.button, { [styles.checked]: isActive });
	const textClassName = cn(styles.text);

	return (
		<button type={type} className={btnClassName} onClick={() => setIsActive(!isActive)}>
			<img src={light.toString()} className={styles.icon} alt="icon" />
			<p className={textClassName}>{text}</p>
		</button>
	);
}

TagButton.propTypes = {
	type: PropTypes.oneOf(['submit', 'button']),
	theme: PropTypes.oneOf(['light', 'dark']),
	tag: PropTypes.oneOf(['alternative', 'roaster', 'milk', 'coffeemachine']),
	active: PropTypes.bool,
};

TagButton.defaultProps = {
	type: 'button',
	theme: 'light',
	tag: 'alternative',
	active: false,
};

export default TagButton;
