module.exports = {
  testEnvironment: 'jsdom',
  transform: {
    '^.+\.(ts|tsx)$': 'ts-jest'
  },
  moduleFileExtensions: ['ts','tsx','js'],
  setupFilesAfterEnv: ['<rootDir>/tests/setupTests.ts']
}
