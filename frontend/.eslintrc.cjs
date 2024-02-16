module.exports = {
	env: {
		browser: true,
		es2023: true,
	},
	extends: [
		'airbnb',
		'eslint:recommended',
		'prettier',
		'plugin:react/recommended',
		'plugin:storybook/recommended',
	],
	overrides: [
		{
			env: {
				node: true,
			},
			files: ['.eslintrc.{js,cjs}'],
			parserOptions: {
				sourceType: 'script',
			},
		},
	],
	parserOptions: {
		ecmaVersion: 'latest',
		sourceType: 'module',
	},
	plugins: ['react', 'prettier'],
	rules: {
		'react/prop-types': 'off',
		'no-var': 'error',
		'prefer-const': 'warn',
		'no-unused-vars': 'off',
		'react/react-in-jsx-scope': 'off',
		'prettier/prettier': ['warn', { endOfLine: 'auto' }],
		'import/prefer-default-export': 'off',
		'react/jsx-props-no-spreading': 'off',
		'react/function-component-definition': 'off',
		'react/button-has-type': 'off',
	},
};
