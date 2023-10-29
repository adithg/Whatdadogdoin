
CREATE DATABASE Dummy
WITH ENGINE = "postgres",
PARAMETERS = {
  "user": "postgres",
  "port": 10392,
  "password": "password",
  "host": "4.tcp.us-cal-1.ngrok.io",
  "database": "Midas"
  -- Other parameters --
  };

-- model to pull data from binance based off the time of a trade
CREATE JOB binance_data AS (
    SELECT *
    FROM my_binance.aggregated_trade_data AS trade
    JOIN Hume.crypto_trades  AS crypto_data
    ON trade.symbol = crypto_data.crypto
    LIMIT 10
);
END '2024-02-01 00:00:00'
EVERY 1/2 day;


-- model to give advice based off the emotion weights and crypto

CREATE MODEL candlelit
PREDICT advice
USING
  engine = 'openai',
  max_tokens = 300,
  temperature = 0.75,
  api_key = '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',
  model_name = 'gpt-4', -- you can also use 'text-davinci-003' or 'gpt-3.5-turbo'
  prompt_template = '

Your are a stock advice bot, your name is midas and you are helping people with their questions answer very spartan.

For user emotion tracking: {{emotion_sigfig_and_emotionweight}}\

and for user trade tracking: {{crypto_and_change}}\

In less than 200 characters, generate advice using the emotion and extent of the emotion as well as the crypto currency invested in and how the trade did. Advise them to invest more if the emotion led to a positive trade, and advise them to stay away from trades when feeling a certain emotion if the trade did poorly.';
-

-- CREATE MODEL mindsdb.emotions_crypto_predictor
-- FROM my_binance,Hume
-- WHERE emotions IS NOT NULL AND crypto_trades IS NOT NULL
-- PREDICT crypto_trades
-- USING engine = 'lightwood',
--       tag = 'emotions crypto trade model';


-- CREATE MODEL EmotionToTrade
-- FROM my_binance,Hume (
--   SELECT * FROM aggregated_trade_data,Emotions
--   WHERE symbol = crypto_data.crypto
--   )
-- PREDICT open_price
-- ORDER BY open_time
-- GROUP BY [group_by];

