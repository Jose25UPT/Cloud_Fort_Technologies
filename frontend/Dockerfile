# Multi-stage build for Vue.js frontend
FROM node:18-alpine as build-stage

# Set working directory
WORKDIR /app

# Create app user and set permissions
RUN addgroup -g 1001 -S nodejs && \
    adduser -S vueapp -u 1001

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy source code
COPY . .

# Change ownership to app user
RUN chown -R vueapp:nodejs /app

# Switch to app user
USER vueapp

# Build the app
RUN npm run build

# Production stage
FROM nginx:alpine as production-stage

# Install curl for health check
RUN apk add --no-cache curl

# Copy built app to nginx
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Copy nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Create nginx user and set permissions
RUN chown -R nginx:nginx /usr/share/nginx/html

# Expose port
EXPOSE 80

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:80/ || exit 1

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
