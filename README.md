# Real-Time Order Book Visualizer

A high-performance, real-time stock order book visualizer built with Next.js, TypeScript, and the Binance WebSocket API.

## Features

- **Real-time WebSocket connection** to Binance API
- **Order Book visualization** with depth charts
- **Recent Trades feed** with flash animations
- **Auto-reconnection** on connection loss
- **Performance optimized** with React.memo, useMemo, and useCallback
- **Minimalistic dark theme** design
- **Fully responsive** layout

## Tech Stack

- **Framework**: Next.js 14
- **Language**: TypeScript
- **Styling**: CSS Modules
- **API**: Binance WebSocket Streams

## Installation

1. Clone the repository
2. Install dependencies:

```bash
npm install
```

## Running the Application

Development mode:
```bash
npm run dev
```

The application will be available at `http://localhost:3000`

Production build:
```bash
npm run build
npm start
```

## Project Structure

```
├── components/
│   ├── OrderBook.tsx       # Order book component with depth visualization
│   └── RecentTrades.tsx    # Recent trades feed with animations
├── hooks/
│   └── useBinanceSocket.ts # Custom hook for WebSocket connection
├── pages/
│   ├── _app.tsx           # Global app wrapper
│   ├── _document.tsx      # HTML document structure
│   └── index.tsx          # Main page
├── styles/
│   ├── globals.css        # Global styles
│   ├── Home.module.css    # Home page styles
│   ├── OrderBook.module.css # Order book styles
│   └── RecentTrades.module.css # Recent trades styles
├── package.json
├── tsconfig.json
└── next.config.js
```

## Design Decisions

### WebSocket Management
- Custom `useBinanceSocket` hook handles all WebSocket logic
- Automatic reconnection with 3-second delay on disconnection
- Combined stream approach for efficiency (aggTrade + depth)
- Buffer management to maintain last 50 trades

### Performance Optimizations
- **React.memo**: Wraps OrderBook, RecentTrades, and row components
- **useMemo**: Calculates sorted order book and cumulative totals
- **useCallback**: Memoizes WebSocket connection function
- **Map data structure**: O(1) updates for order book price levels
- **CSS transitions**: Hardware-accelerated for smooth animations

### State Management
- Local component state with React hooks (no external library needed)
- Efficient updates prevent unnecessary re-renders
- Reference-based optimization for trades buffer

### UI/UX
- Binance-inspired dark theme for familiarity
- Color coding: Green (bids/buys), Red (asks/sells), Yellow (spread)
- Flash animations on new trades for visibility
- Depth bars show cumulative volume visually
- Responsive grid layout adapts to screen size

## API Integration

### Streams Used
1. **Aggregate Trades**: `btcusdt@aggTrade`
   - Provides recent completed trades
   - Includes price, quantity, time, and trade direction

2. **Order Book Depth**: `btcusdt@depth@100ms`
   - Updates every 100ms
   - Provides bid/ask price levels with quantities
   - 0 quantity = remove price level

### Connection Details
- WebSocket URL: `wss://stream.binance.com:9443/stream`
- Trading Pair: BTC/USDT
- Update Speed: 100ms (high-frequency)
- Auto-reconnect on failure

## Performance Considerations

- Minimal re-renders through memoization
- Efficient data structures (Map for O(1) lookups)
- Limited order book display (15 levels each side)
- CSS-based animations (GPU-accelerated)
- No external state management libraries
- Lightweight bundle size

## Deployment

The application is optimized for deployment on:
- **Vercel** (recommended for Next.js)
- **Netlify**
- Any platform supporting Node.js

To deploy on Vercel:
```bash
npm install -g vercel
vercel
```

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Opera (latest)

WebSocket API is supported in all modern browsers.

## License

MIT