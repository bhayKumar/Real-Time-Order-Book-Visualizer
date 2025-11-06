// hooks/useBinanceSocket.ts
import { useEffect, useRef, useState, useCallback } from 'react';

export interface Trade {
  price: string;
  quantity: string;
  time: number;
  isBuyerMaker: boolean;
}

export interface OrderBookUpdate {
  bids: [string, string][];
  asks: [string, string][];
}

interface BinanceSocketData {
  trades: Trade[];
  orderBook: OrderBookUpdate | null;
  isConnected: boolean;
}

const BINANCE_WS_URL = 'wss://stream.binance.com:9443/stream';
const SYMBOL = 'btcusdt';
const RECONNECT_DELAY = 3000;
const MAX_TRADES = 50;

export const useBinanceSocket = (): BinanceSocketData => {
  const [trades, setTrades] = useState<Trade[]>([]);
  const [orderBook, setOrderBook] = useState<OrderBookUpdate | null>(null);
  const [isConnected, setIsConnected] = useState(false);
  const wsRef = useRef<WebSocket | null>(null);
  const reconnectTimeoutRef = useRef<NodeJS.Timeout | null>(null);
  const tradesBufferRef = useRef<Trade[]>([]);

  const connect = useCallback(() => {
    try {
      const streams = [
        `${SYMBOL}@aggTrade`,
        `${SYMBOL}@depth@100ms`
      ];
      const url = `${BINANCE_WS_URL}?streams=${streams.join('/')}`;
      
      const ws = new WebSocket(url);
      wsRef.current = ws;

      ws.onopen = () => {
        setIsConnected(true);
        console.log('WebSocket connected');
      };

      ws.onmessage = (event) => {
        try {
          const message = JSON.parse(event.data);
          const { stream, data } = message;

          if (stream.includes('@aggTrade')) {
            const trade: Trade = {
              price: data.p,
              quantity: data.q,
              time: data.T,
              isBuyerMaker: data.m
            };
            
            tradesBufferRef.current = [trade, ...tradesBufferRef.current.slice(0, MAX_TRADES - 1)];
            setTrades([...tradesBufferRef.current]);
          } else if (stream.includes('@depth')) {
            setOrderBook({
              bids: data.b,
              asks: data.a
            });
          }
        } catch (error) {
          console.error('Error parsing WebSocket message:', error);
        }
      };

      ws.onerror = (error) => {
        console.error('WebSocket error:', error);
        setIsConnected(false);
      };

      ws.onclose = () => {
        setIsConnected(false);
        console.log('WebSocket closed, attempting to reconnect...');
        
        reconnectTimeoutRef.current = setTimeout(() => {
          connect();
        }, RECONNECT_DELAY);
      };
    } catch (error) {
      console.error('Error creating WebSocket connection:', error);
    }
  }, []);

  useEffect(() => {
    connect();

    return () => {
      if (reconnectTimeoutRef.current) {
        clearTimeout(reconnectTimeoutRef.current);
      }
      if (wsRef.current) {
        wsRef.current.close();
      }
    };
  }, [connect]);

  return { trades, orderBook, isConnected };
};