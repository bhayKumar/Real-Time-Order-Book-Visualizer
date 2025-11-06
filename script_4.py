
# Create the main page component
main_page = """
// pages/index.tsx
import React from 'react';
import { useBinanceSocket } from '../hooks/useBinanceSocket';
import { OrderBook } from '../components/OrderBook';
import { RecentTrades } from '../components/RecentTrades';
import styles from '../styles/Home.module.css';

export default function Home() {
  const { trades, orderBook, isConnected } = useBinanceSocket();

  return (
    <div className={styles.container}>
      <header className={styles.header}>
        <h1>Real-Time Order Book Visualizer</h1>
        <div className={`${styles.status} ${isConnected ? styles.connected : styles.disconnected}`}>
          {isConnected ? '● Connected' : '● Disconnected'}
        </div>
      </header>
      
      <main className={styles.main}>
        <div className={styles.orderBookWrapper}>
          {orderBook ? (
            <OrderBook bids={orderBook.bids} asks={orderBook.asks} />
          ) : (
            <div className={styles.loading}>Loading order book...</div>
          )}
        </div>
        
        <div className={styles.tradesWrapper}>
          <RecentTrades trades={trades} />
        </div>
      </main>
    </div>
  );
}
"""

print("Main page component created:")
print("pages/index.tsx")
print("\nKey features:")
print("- Clean, minimalistic layout")
print("- Connection status indicator")
print("- OrderBook and RecentTrades side by side")
print("- Loading state handling")
