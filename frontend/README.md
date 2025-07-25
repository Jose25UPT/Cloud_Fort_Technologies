# CloudFort Technologies - Frontend

Vue.js 3 + TypeScript + Tailwind CSS frontend application.

## 🛠️ Tech Stack

- **Vue.js 3** - Composition API
- **TypeScript** - Type safety
- **Tailwind CSS** - Utility-first CSS
- **Vite** - Build tool
- **Pinia** - State management
- **Vue Router** - Routing
- **Axios** - HTTP client
- **Headless UI** - Accessible components

## 📁 Project Structure

```
src/
├── assets/          # Static assets (images, styles)
├── components/      # Reusable Vue components
├── layouts/         # Layout components
├── pages/          # Page components
├── router/         # Vue Router configuration
├── store/          # Pinia stores
├── services/       # API services
├── utils/          # Utility functions
├── App.vue         # Root component
└── main.ts         # Application entry point
```

## 🚀 Development

### Prerequisites
- Node.js 18+ 
- npm or yarn

### Setup
```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

### Code Quality
```bash
# Type checking
npm run type-check

# Linting
npm run lint

# Format code
npm run format
```

## 🎨 Styling

This project uses Tailwind CSS for styling with custom theme extensions defined in `tailwind.config.js`.

### Custom Colors
- Primary: Blue scale (50-950)
- Custom brand colors can be added to the theme

### Components
- Headless UI components for accessibility
- Custom component library in `src/components/`

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the frontend directory:
```env
VITE_API_URL=http://localhost:8000
VITE_APP_NAME="CloudFort Technologies"
```

### API Integration
- Axios instance configured in `src/services/api.ts`
- Base URL from environment variables
- Interceptors for auth tokens and error handling

## 🏗️ Build & Deploy

### Docker
The frontend includes a Dockerfile for containerized deployment.

### Static Build
```bash
npm run build
# Output in dist/ directory
```

## 📝 Notes

- Uses Vite proxy for API calls in development
- Hot module replacement enabled
- TypeScript strict mode enabled
- ESLint + Prettier configured
