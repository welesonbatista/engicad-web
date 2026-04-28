CREATE TABLE parts (
    id UUID PRIMARY KEY,
    diameter NUMERIC,
    length NUMERIC,
    hole_diameter NUMERIC,
    file_path TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
CREATE TABLE part_generation_logs (
    id UUID PRIMARY KEY,
    part_id UUID REFERENCES parts(id),
    status VARCHAR(50),
    message TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);