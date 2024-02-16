import styles from './TagSection.module.scss';
import { BASE_TAGS } from '../../utils/constants';

import TagButton from '../../assets/ui-kit/TagButton/TagButton';
import HorizontalLine from '../HorizontalLine/HorizontalLine';

function TagSection() {
	return (
		<>
			<section className={styles.tags}>
				<ul>
					{BASE_TAGS.map(item => (
						<li key={item.id}>
							<TagButton text={item.text} tag={item.tag} />
						</li>
					))}
				</ul>
			</section>
			<HorizontalLine />
		</>
	);
}

export default TagSection;
