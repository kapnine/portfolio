FROM node:lts-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the application code
COPY . .

# Build the Vue app
RUN npm run build

# Expose the application port
EXPOSE 3000

CMD ["npx", "serve", "-s", "dist", "-l", "3000"]
