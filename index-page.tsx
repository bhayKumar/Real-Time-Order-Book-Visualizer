import React from 'react';
import { useBinanceSocket } from './hooks/useBinanceSocket';
import { OrderBook } from './components/OrderBook';
import { RecentTrades } from './components/RecentTrades';

const containerStyle: React.CSSProperties = {
  fontFamily: 'var(--font-family-base, system-ui, sans-serif)',
  padding: 24,
  maxWidth: 1200,
  margin: '0 auto'
};

const headerStyle: React.CSSProperties = {
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'space-between',
  marginBottom: 16
};

const statusBase: React.CSSProperties = {
  padding: '6px 10px',
  borderRadius: 8,
  fontSize: 14
};

const mainStyle: React.CSSProperties = {
  display: 'grid',
  gridTemplateColumns: '1fr 360px',
  gap: 20,
  alignItems: 'start'
};

export default function Home() {
  const { trades, orderBook, isConnected } = useBinanceSocket();

  return (
    <div style={containerStyle}>
      <header style={headerStyle}>
        <h1>Real-Time Order Book Visualizer</h1>
        <div
          style={{
            ...statusBase,
            background: isConnected ? 'rgba(33,128,141,0.12)' : 'rgba(192,21,47,0.06)',
            color: isConnected ? 'var(--color-success)' : 'var(--color-error)'
          }}
        >
          {isConnected ? '● Connected' : '● Disconnected'}
        </div>
      </header>

      <main style={mainStyle}>
        <div>
          {orderBook ? (
            <OrderBook bids={orderBook.bids} asks={orderBook.asks} />
          ) : (
            <div style={{ padding: 24 }}>Loading order book...</div>
          )}
        </div>

        <aside>
          <RecentTrades trades={trades} />
        </aside>
      </main>
    </div>
  );
}