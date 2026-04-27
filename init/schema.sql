CREATE TABLE parts (
    id UUID PRIMARY KEY,
    diameter NUMERIC NOT NULL,
    length NUMERIC NOT NULL,
    hole_diameter NUMERIC NOT NULL,
    file_path TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
CREATE TABLE part_generation_logs (
    id UUID PRIMARY KEY,
    part_id UUID REFERENCES parts(id),
    status VARCHAR(50),
    message TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);