import PropTypes from 'prop-types';
import cn from 'classnames';
import styles from './Button.module.scss';

function Button({ type, text, size }) {
	const btnClassName = cn(styles.button, styles[size]);

	return (
		<button type={type} className={btnClassName}>
			<p>{text}</p>
		</button>
	);
}

Button.propTypes = {
	type: PropTypes.oneOf(['submit', 'button']),
	size: PropTypes.oneOf(['large', 'small']),
};

Button.defaultProps = {
	type: 'button',
	size: 'large',
};

export default Button;
