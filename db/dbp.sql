-- Supabase AI is experimental and may produce incorrect answers
-- Always verify the output before executing

-- Crear la tabla USER
create table
  users (
    id bigint primary key generated always as identity,
    name text not null,
    email text unique not null,
    hashed_password text not null,
    type text check (
      type in ('3', '4', '2', '1')
    ) not null,
    eco_points integer default 0
  );

-- Crear la tabla MATERIAL
create table
  material (
    id bigint primary key generated always as identity,
    name text unique not null,
    points_per_kg float not null
  );

-- Crear la tabla RECYCLING_POINT
create table
  recycling_points (
    id bigint primary key generated always as identity,
    name text not null,
    latitude float not null,
    longitude float not null,
    current_capacity integer not null,
    max_capacity integer not null
  );

-- Crear la tabla RECYCLING
create table
  recycling (
    id bigint primary key generated always as identity,
    user_id integer references users (id),
    material_id integer references material (id),
    weight float not null,
    date timestamp default current_timestamp,
    earned_points integer not null,
    recycling_point_id integer references recycling_points (id)
  );

-- Crear la tabla REWARD
create table
  rewards (
    id bigint primary key generated always as identity,
    name text not null,
    description text,
    cost_points integer not null
  );

-- Crear la tabla REEDEM_HISTORY
create table
  redeem_history (
    id bigint primary key generated always as identity,
    user_id integer references users (id),
    reward_id integer references rewards (id),
    date timestamp default current_timestamp
  );

-- Crear la tabla ACHIEVEMENT
create table
  achivements (
    id bigint primary key generated always as identity,
    name text not null,
    description text,
    required_points integer not null
  );

-- Crear la tabla intermedia USER_ACHIEVEMENT para la relación muchos a muchos
create table
  user_achievements (
    user_id integer references users (id),
    achievement_id integer references achivements (id),
    date_obtained timestamp default current_timestamp,
    primary key (user_id, achievement_id)
  );

-- Crear la tabla POINT_TRANSACTION
create table
  point_transactions (
    id bigint primary key generated always as identity,
    user_id integer references users (id),
    points integer not null,
    type text check (
      type in ('earned', 'redeemed')
    ) not null,
    date timestamp default current_timestamp
  );

-- Crear la tabla REPORT
create table
  reports (
    id bigint primary key generated always as identity,
    start_date timestamp not null,
    end_date timestamp not null,
    data JSONB not null
  );

-- Crear índices para mejorar el rendimiento de las consultas frecuentes
create index idx_recycling_user_id on recycling (user_id);

create index idx_recycling_material_id on recycling (material_id);

create index idx_recycling_date on recycling (date);

create index idx_point_transactions_user_id on point_transactions (user_id);

create index idx_point_transactions_date on point_transactions (date);

create index idx_reedem_history_user_id on redeem_history (user_id);

create index idx_redeem_history_reward_id on redeem_history (reward_id);